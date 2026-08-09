export const stripePaymentLink = process.env.NEXT_PUBLIC_STRIPE_PAYMENT_LINK || "";

export const hasValidStripePaymentLink = /^https:\/\/buy\.stripe\.com\//.test(stripePaymentLink);

export const supporterPrice = "$19";

export function trackMonetizationEvent(eventName: string, extra: Record<string, string> = {}) {
  if (typeof window === "undefined") return;

  const gtag = (window as typeof window & {
    gtag?: (command: "event", eventName: string, params: Record<string, string>) => void;
  }).gtag;

  gtag?.("event", eventName, {
    event_category: "monetization_validation",
    payment_link_state: hasValidStripePaymentLink ? "configured" : "missing",
    ...extra,
  });
}
