export default function LegalDisclosure() {
  const rows = [
    ["Product / Public Brand Name", "NonMouse"],
    ["Seller's Name or Legal Name", "Disclosed without delay upon request from a consumer."],
    ["Responsible Person", "Disclosed without delay upon request from a consumer."],
    ["Address", "Disclosed without delay upon request from a consumer."],
    ["Phone Number", "Disclosed without delay upon request from a consumer."],
    ["Email", "kintre.ndy0@gmail.com"],
    ["Website / Sales URL", "https://nonmouse.com/"],
    [
      "Product / Service",
      "NonMouse software access, early-access builds, supporter digital benefits, setup/support benefits, or voluntary supporter payments without additional benefits.",
    ],
  ];

  const sections = [
    ["Price", "The price, including applicable taxes where shown, is displayed on each sales, supporter, or checkout page."],
    [
      "Additional Fees",
      "Customers are responsible for internet access, data charges, payment-provider fees, currency-conversion fees, and other costs separately charged by their network, bank, card issuer, or payment platform.",
    ],
    [
      "Payment Method and Timing",
      "Payments are processed by the payment methods offered by Buy Me a Coffee, Ko-fi, credit-card processors, or any other checkout provider listed at the point of purchase. Payment is charged when the purchase or supporter payment is completed.",
    ],
    [
      "Delivery Timing",
      "Unless a sales page states otherwise, digital products or early-access benefits are delivered after payment is completed. Voluntary supporter payments without stated benefits do not include a separate product or service in return.",
    ],
    [
      "Returns, Cancellations, and Refunds",
      "Because NonMouse paid offerings are digital products or supporter payments, returns, cancellations, and refunds are generally not available after purchase. We will review cases such as duplicate payments, inability to deliver the purchased item, or a material difference from the sales-page description. To request review, email us with the purchase date, purchase URL, and reason. Refund handling is subject to the rules and technical capabilities of the relevant payment platform.",
    ],
    [
      "System Requirements",
      "System requirements are described on the NonMouse website, GitHub repository, distribution page, or relevant sales page.",
    ],
    [
      "Disclosure of Seller's Name or Legal Name, Address, Phone Number, and Responsible Person",
      "NonMouse is the public product/brand name, not a seller name used to replace the legal disclosure items. Under Japan's Act on Specified Commercial Transactions, the seller's name or legal name, address, phone number, and responsible person may be omitted from public display if they are disclosed without delay upon a consumer's request. To request disclosure, contact the email address above.",
    ],
    ["Contact", "Email: kintre.ndy0@gmail.com\nWe usually reply within 3 business days."],
  ];

  return (
    <div className="min-h-screen bg-background py-24">
      <div className="container px-4 mx-auto max-w-3xl">
        <h1 className="text-4xl font-bold mb-6">Commerce Disclosure</h1>
        <p className="text-muted-foreground mb-4">Last updated: 2026-08-22</p>
        <p className="text-muted-foreground mb-10">
          This page provides NonMouse's disclosure for paid digital offerings and supporter payments, including information required by Japan's Act on Specified Commercial Transactions (特定商取引法).
        </p>

        <div className="space-y-10 text-base leading-8">
          <section>
            <h2 className="text-2xl font-semibold mb-6">Seller Information</h2>
            <div className="space-y-6">
              {rows.map(([label, value]) => (
                <div key={label} className="border-b border-border pb-5">
                  <h3 className="font-semibold mb-2">{label}</h3>
                  <p className="whitespace-pre-line text-muted-foreground">{value}</p>
                </div>
              ))}
            </div>
          </section>

          {sections.map(([title, body]) => (
            <section key={title}>
              <h2 className="text-2xl font-semibold mb-4">{title}</h2>
              <p className="whitespace-pre-line text-muted-foreground">{body}</p>
            </section>
          ))}
        </div>
      </div>
    </div>
  );
}
