# cloud-security

A static cloud security cheatsheet covering AWS, Azure, and GCP. Built
as a learning resource for offensive and defensive cloud testing.

Live at: [zhameersheraz.github.io/cloud-security](https://zhameersheraz.github.io/cloud-security/)

## Pages

| Page         | Topic                                          |
| ------------ | ---------------------------------------------- |
| `index.html` | Landing                                        |
| `aws.html`   | AWS misconfigurations, tools, useful commands  |
| `azure.html` | Azure misconfigurations, tools, useful commands|
| `gcp.html`   | GCP misconfigurations, tools, useful commands  |
| `tools.html` | Curated cloud security tool directory          |

## Run locally

Any static file server works. The simplest:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

Or with Node:

```bash
npx serve .
```

## Deployment

This site is static, so it deploys anywhere. Two easy options:

- **GitHub Pages** &mdash; repo Settings &rarr; Pages &rarr; Source: `main` / root
- **Vercel** &mdash; import the GitHub repo at vercel.com, no config needed

Every push to `main` redeploys.

## Source structure

```
cloud-security/
├── index.html      # landing
├── aws.html        # AWS cheatsheet
├── azure.html      # Azure cheatsheet
├── gcp.html        # GCP cheatsheet
├── tools.html      # tool directory
├── styles.css      # shared theme
├── script.js       # mobile menu + copy-to-clipboard
├── package.json    # for Vercel
└── vercel.json     # Vercel config
```

## How to contribute

Found a misconfiguration that's missing? Edit the relevant HTML file
and open a PR. No build step, no framework &mdash; just edit and refresh.

## Author

Zhameer Sheraz Tampugao &mdash; [github.com/zhameersheraz](https://github.com/zhameersheraz)

## License

MIT &mdash; see [LICENSE](LICENSE).
