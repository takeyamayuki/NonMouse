# NonMouse Website

This directory contains the full source for the NonMouse landing page, not just the generated HTML/CSS output.

## Stack

- Next.js App Router
- TypeScript
- Tailwind CSS
- Static export via `next build`

## Local development

```sh
npm install
npm run dev
```

To preview with the optional supporter checkout CTA enabled, set a Buy Me a Coffee link:

```sh
NEXT_PUBLIC_BUY_ME_A_COFFEE_LINK=https://buymeacoffee.com/bamboo_dev npm run dev
NEXT_PUBLIC_KO_FI_LINK=https://ko-fi.com/bamboo_dev npm run dev
```

The Buy Me a Coffee URL must start with `https://buymeacoffee.com/`, and the Ko-fi URL must start with `https://ko-fi.com/`. If every support URL is missing or invalid, support buttons are disabled instead of linking to a broken payment page.

## Build

```sh
npm run lint
npm run build
```

The hero demo uses an animated NonMouse demo asset from the main GitHub README so the landing page shows the product in action without relying on the old broken embedded video provider.
