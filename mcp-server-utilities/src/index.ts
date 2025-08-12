#!/usr/bin/env node
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';
import axios from 'axios';
import * as cheerio from 'cheerio';
import JSON5 from 'json5';
import * as yaml from 'yaml';
import { parseString as parseXml } from 'xml2js';
import { parse as parseCsv } from 'csv-parse/sync';
import { stringify as stringifyCsv } from 'csv-stringify/sync';
import { diffLines, diffWords, diffChars } from 'diff';
import { JSONPath } from 'jsonpath-plus';
import { promisify } from 'util';
import crypto from 'crypto';
import { URL } from 'url';

const parseXmlAsync = promisify(parseXml);

class UtilitiesServer {
  private server: Server;

  constructor() {
    this.server = new Server(
      {
        name: 'mcp-server-utilities',
        version: '1.0.0',
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );

    this.setupHandlers();
  }

  private setupHandlers() {
    this.server.setRequestHandler(ListToolsRequestSchema, async () => ({
      tools: [
        {
          name: 'parse_json5',
          description: 'Parse JSON5 format (JSON with comments, trailing commas, unquoted keys)',
          inputSchema: {
            type: 'object',
            properties: {
              content: {
                type: 'string',
                description: 'JSON5 content to parse',
              },
            },
            required: ['content'],
          },
        },
        {
          name: 'parse_yaml',
          description: 'Parse YAML content into JSON',
          inputSchema: {
            type: 'object',
            properties: {
              content: {
                type: 'string',
                description: 'YAML content to parse',
              },
            },
            required: ['content'],
          },
        },
        {
          name: 'parse_xml',
          description: 'Parse XML content into JSON',
          inputSchema: {
            type: 'object',
            properties: {
              content: {
                type: 'string',
                description: 'XML content to parse',
              },
            },
            required: ['content'],
          },
        },
        {
          name: 'parse_csv',
          description: 'Parse CSV content into JSON array',
          inputSchema: {
            type: 'object',
            properties: {
              content: {
                type: 'string',
                description: 'CSV content to parse',
              },
              delimiter: {
                type: 'string',
                description: 'Column delimiter (default: ",")',
              },
              has_headers: {
                type: 'boolean',
                description: 'First row contains headers (default: true)',
              },
            },
            required: ['content'],
          },
        },
        {
          name: 'to_csv',
          description: 'Convert JSON array to CSV format',
          inputSchema: {
            type: 'object',
            properties: {
              data: {
                type: 'array',
                description: 'Array of objects to convert to CSV',
              },
              delimiter: {
                type: 'string',
                description: 'Column delimiter (default: ",")',
              },
              headers: {
                type: 'boolean',
                description: 'Include headers row (default: true)',
              },
            },
            required: ['data'],
          },
        },
        {
          name: 'to_yaml',
          description: 'Convert JSON to YAML format',
          inputSchema: {
            type: 'object',
            properties: {
              data: {
                type: 'object',
                description: 'JSON data to convert to YAML',
              },
            },
            required: ['data'],
          },
        },
        {
          name: 'extract_html_text',
          description: 'Extract text content from HTML, removing all tags',
          inputSchema: {
            type: 'object',
            properties: {
              html: {
                type: 'string',
                description: 'HTML content to extract text from',
              },
            },
            required: ['html'],
          },
        },
        {
          name: 'extract_html_links',
          description: 'Extract all links (href attributes) from HTML',
          inputSchema: {
            type: 'object',
            properties: {
              html: {
                type: 'string',
                description: 'HTML content to extract links from',
              },
              base_url: {
                type: 'string',
                description: 'Base URL to resolve relative links',
              },
            },
            required: ['html'],
          },
        },
        {
          name: 'query_html',
          description: 'Query HTML using CSS selectors (cheerio/jQuery-like)',
          inputSchema: {
            type: 'object',
            properties: {
              html: {
                type: 'string',
                description: 'HTML content to query',
              },
              selector: {
                type: 'string',
                description: 'CSS selector to query',
              },
              attribute: {
                type: 'string',
                description: 'Attribute to extract (optional, defaults to text content)',
              },
            },
            required: ['html', 'selector'],
          },
        },
        {
          name: 'jsonpath_query',
          description: 'Query JSON data using JSONPath expressions',
          inputSchema: {
            type: 'object',
            properties: {
              data: {
                type: 'object',
                description: 'JSON data to query',
              },
              path: {
                type: 'string',
                description: 'JSONPath expression (e.g., "$.store.book[*].author")',
              },
            },
            required: ['data', 'path'],
          },
        },
        {
          name: 'diff_text',
          description: 'Compare two texts and show differences',
          inputSchema: {
            type: 'object',
            properties: {
              text1: {
                type: 'string',
                description: 'First text to compare',
              },
              text2: {
                type: 'string',
                description: 'Second text to compare',
              },
              mode: {
                type: 'string',
                enum: ['lines', 'words', 'chars'],
                description: 'Diff mode (default: lines)',
              },
            },
            required: ['text1', 'text2'],
          },
        },
        {
          name: 'generate_hash',
          description: 'Generate hash of text using various algorithms',
          inputSchema: {
            type: 'object',
            properties: {
              text: {
                type: 'string',
                description: 'Text to hash',
              },
              algorithm: {
                type: 'string',
                enum: ['md5', 'sha1', 'sha256', 'sha512'],
                description: 'Hash algorithm (default: sha256)',
              },
            },
            required: ['text'],
          },
        },
        {
          name: 'base64_encode',
          description: 'Encode text to base64',
          inputSchema: {
            type: 'object',
            properties: {
              text: {
                type: 'string',
                description: 'Text to encode',
              },
            },
            required: ['text'],
          },
        },
        {
          name: 'base64_decode',
          description: 'Decode base64 to text',
          inputSchema: {
            type: 'object',
            properties: {
              encoded: {
                type: 'string',
                description: 'Base64 encoded string',
              },
            },
            required: ['encoded'],
          },
        },
        {
          name: 'url_parse',
          description: 'Parse URL into components',
          inputSchema: {
            type: 'object',
            properties: {
              url: {
                type: 'string',
                description: 'URL to parse',
              },
            },
            required: ['url'],
          },
        },
        {
          name: 'generate_uuid',
          description: 'Generate a random UUID v4',
          inputSchema: {
            type: 'object',
            properties: {},
          },
        },
        {
          name: 'format_json',
          description: 'Format/prettify JSON with indentation',
          inputSchema: {
            type: 'object',
            properties: {
              data: {
                type: 'object',
                description: 'JSON data to format',
              },
              indent: {
                type: 'number',
                description: 'Number of spaces for indentation (default: 2)',
              },
            },
            required: ['data'],
          },
        },
        {
          name: 'minify_json',
          description: 'Minify JSON by removing whitespace',
          inputSchema: {
            type: 'object',
            properties: {
              data: {
                type: 'object',
                description: 'JSON data to minify',
              },
            },
            required: ['data'],
          },
        },
        {
          name: 'escape_regex',
          description: 'Escape special characters in a string for use in regex',
          inputSchema: {
            type: 'object',
            properties: {
              text: {
                type: 'string',
                description: 'Text to escape for regex',
              },
            },
            required: ['text'],
          },
        },
        {
          name: 'calculate_statistics',
          description: 'Calculate basic statistics for an array of numbers',
          inputSchema: {
            type: 'object',
            properties: {
              numbers: {
                type: 'array',
                items: { type: 'number' },
                description: 'Array of numbers',
              },
            },
            required: ['numbers'],
          },
        },
      ],
    }));

    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { name, arguments: args = {} } = request.params;

      try {
        switch (name) {
          case 'parse_json5':
            return {
              content: [
                {
                  type: 'text',
                  text: JSON.stringify(JSON5.parse(args.content as string), null, 2),
                },
              ],
            };

          case 'parse_yaml':
            return {
              content: [
                {
                  type: 'text',
                  text: JSON.stringify(yaml.parse(args.content as string), null, 2),
                },
              ],
            };

          case 'parse_xml':
            const xmlResult = await parseXmlAsync(args.content as string);
            return {
              content: [
                {
                  type: 'text',
                  text: JSON.stringify(xmlResult, null, 2),
                },
              ],
            };

          case 'parse_csv':
            const csvData = parseCsv(args.content as string, {
              delimiter: (args.delimiter as string) || ',',
              columns: args.has_headers !== false,
            });
            return {
              content: [
                {
                  type: 'text',
                  text: JSON.stringify(csvData, null, 2),
                },
              ],
            };

          case 'to_csv':
            const csv = stringifyCsv(args.data as any[], {
              delimiter: (args.delimiter as string) || ',',
              header: args.headers !== false,
            });
            return {
              content: [
                {
                  type: 'text',
                  text: csv,
                },
              ],
            };

          case 'to_yaml':
            return {
              content: [
                {
                  type: 'text',
                  text: yaml.stringify(args.data),
                },
              ],
            };

          case 'extract_html_text':
            const $ = cheerio.load(args.html as string);
            return {
              content: [
                {
                  type: 'text',
                  text: $.text().trim(),
                },
              ],
            };

          case 'extract_html_links':
            const $links = cheerio.load(args.html as string);
            const links: string[] = [];
            $links('a[href]').each((_, el) => {
              let href = $links(el).attr('href');
              if (href && args.base_url) {
                try {
                  href = new URL(href, args.base_url as string).href;
                } catch {}
              }
              if (href) links.push(href);
            });
            return {
              content: [
                {
                  type: 'text',
                  text: JSON.stringify(links, null, 2),
                },
              ],
            };

          case 'query_html':
            const $query = cheerio.load(args.html as string);
            const elements = $query(args.selector as string);
            const results: any[] = [];
            elements.each((_, el) => {
              if (args.attribute) {
                results.push($query(el).attr(args.attribute as string));
              } else {
                results.push($query(el).text().trim());
              }
            });
            return {
              content: [
                {
                  type: 'text',
                  text: JSON.stringify(results, null, 2),
                },
              ],
            };

          case 'jsonpath_query':
            const result = JSONPath({
              path: args.path as string,
              json: args.data as any,
            });
            return {
              content: [
                {
                  type: 'text',
                  text: JSON.stringify(result, null, 2),
                },
              ],
            };

          case 'diff_text':
            let diff;
            const mode = (args.mode as string) || 'lines';
            if (mode === 'words') {
              diff = diffWords(args.text1 as string, args.text2 as string);
            } else if (mode === 'chars') {
              diff = diffChars(args.text1 as string, args.text2 as string);
            } else {
              diff = diffLines(args.text1 as string, args.text2 as string);
            }
            
            let output = '';
            diff.forEach(part => {
              const prefix = part.added ? '+' : part.removed ? '-' : ' ';
              output += part.value.split('\n').map(line => prefix + line).join('\n');
            });
            
            return {
              content: [
                {
                  type: 'text',
                  text: output,
                },
              ],
            };

          case 'generate_hash':
            const algorithm = (args.algorithm as string) || 'sha256';
            const hash = crypto.createHash(algorithm).update(args.text as string).digest('hex');
            return {
              content: [
                {
                  type: 'text',
                  text: hash,
                },
              ],
            };

          case 'base64_encode':
            return {
              content: [
                {
                  type: 'text',
                  text: Buffer.from(args.text as string).toString('base64'),
                },
              ],
            };

          case 'base64_decode':
            return {
              content: [
                {
                  type: 'text',
                  text: Buffer.from(args.encoded as string, 'base64').toString('utf-8'),
                },
              ],
            };

          case 'url_parse':
            const url = new URL(args.url as string);
            return {
              content: [
                {
                  type: 'text',
                  text: JSON.stringify({
                    href: url.href,
                    protocol: url.protocol,
                    host: url.host,
                    hostname: url.hostname,
                    port: url.port,
                    pathname: url.pathname,
                    search: url.search,
                    searchParams: Object.fromEntries(url.searchParams),
                    hash: url.hash,
                  }, null, 2),
                },
              ],
            };

          case 'generate_uuid':
            return {
              content: [
                {
                  type: 'text',
                  text: crypto.randomUUID(),
                },
              ],
            };

          case 'format_json':
            return {
              content: [
                {
                  type: 'text',
                  text: JSON.stringify(args.data, null, (args.indent as number) || 2),
                },
              ],
            };

          case 'minify_json':
            return {
              content: [
                {
                  type: 'text',
                  text: JSON.stringify(args.data),
                },
              ],
            };

          case 'escape_regex':
            const escaped = (args.text as string).replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
            return {
              content: [
                {
                  type: 'text',
                  text: escaped,
                },
              ],
            };

          case 'calculate_statistics':
            const numbers = args.numbers as number[];
            const sorted = [...numbers].sort((a, b) => a - b);
            const sum = numbers.reduce((a, b) => a + b, 0);
            const mean = sum / numbers.length;
            const median = sorted.length % 2 === 0
              ? (sorted[sorted.length / 2 - 1] + sorted[sorted.length / 2]) / 2
              : sorted[Math.floor(sorted.length / 2)];
            const variance = numbers.reduce((acc, n) => acc + Math.pow(n - mean, 2), 0) / numbers.length;
            const stdDev = Math.sqrt(variance);
            
            return {
              content: [
                {
                  type: 'text',
                  text: JSON.stringify({
                    count: numbers.length,
                    sum: sum,
                    mean: mean,
                    median: median,
                    min: sorted[0],
                    max: sorted[sorted.length - 1],
                    variance: variance,
                    standardDeviation: stdDev,
                    range: sorted[sorted.length - 1] - sorted[0],
                  }, null, 2),
                },
              ],
            };

          default:
            throw new Error(`Unknown tool: ${name}`);
        }
      } catch (error: any) {
        return {
          content: [
            {
              type: 'text',
              text: `Error: ${error.message}`,
            },
          ],
        };
      }
    });
  }

  async run() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error('MCP Utilities Server running on stdio');
  }
}

const server = new UtilitiesServer();
server.run().catch(console.error);