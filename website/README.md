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

To preview with the optional supporter checkout CTA enabled, set a Stripe Payment Link:

```sh
NEXT_PUBLIC_STRIPE_PAYMENT_LINK=https://buy.stripe.com/... npm run dev
```

The checkout URL must start with `https://buy.stripe.com/`. If it is missing or invalid, checkout buttons are disabled instead of linking to a broken payment page.

## Build

```sh
npm run lint
npm run build
```

The hero demo uses an animated NonMouse demo asset from the main GitHub README so the landing page shows the product in action without relying on the old broken embedded video provider.
