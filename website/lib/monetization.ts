export const supporterPaymentLink =
  process.env.NEXT_PUBLIC_BUY_ME_A_COFFEE_LINK || "https://buymeacoffee.com/bamboo_dev";

export const hasValidSupporterPaymentLink = /^https:\/\/buymeacoffee\.com\//.test(supporterPaymentLink);

export function trackMonetizationEvent(eventName: string, extra: Record<string, string> = {}) {
  if (typeof window === "undefined") return;

  const gtag = (window as typeof window & {
    gtag?: (command: "event", eventName: string, params: Record<string, string>) => void;
  }).gtag;

  gtag?.("event", eventName, {
    event_category: "monetization_validation",
    payment_link_state: hasValidSupporterPaymentLink ? "configured" : "missing",
    ...extra,
  });
}
