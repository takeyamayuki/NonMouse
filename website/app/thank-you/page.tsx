"use client";

import { useEffect } from "react";
import Link from "next/link";
import { Github, Mail, ArrowLeft, Download } from "lucide-react";
import { Button } from "@/components/ui/button";

export default function ThankYouPage() {
  useEffect(() => {
    const gtag = (window as typeof window & {
      gtag?: (command: "event", eventName: string, params: Record<string, unknown>) => void;
    }).gtag;

    const purchaseParams = {
      event_category: "supporter_purchase",
      payment_link_state: "configured",
      currency: "USD",
      items: [
        {
          item_id: "nonmouse_support",
          item_name: "NonMouse Support",
          item_category: "support",
        },
      ],
    };

    gtag?.("event", "purchase", purchaseParams);
    gtag?.("event", "supporter_purchase", purchaseParams);
  }, []);

  return (
    <main className="min-h-screen bg-background">
      <section className="py-24">
        <div className="container px-4 mx-auto max-w-3xl">
          <div className="rounded-3xl border bg-card p-8 md:p-12 shadow-sm">
            <p className="text-sm font-medium text-muted-foreground mb-4">NonMouse Early Access</p>
            <h1 className="text-4xl md:text-5xl font-bold mb-6">Thank you for supporting NonMouse.</h1>
            <p className="text-lg text-muted-foreground mb-8 leading-relaxed">
              Your support helps keep NonMouse moving forward. A receipt and payment details will be sent by the payment provider to the email address used at checkout.
            </p>

            <div className="grid gap-4 mb-10">
              <div className="rounded-2xl bg-accent p-5">
                <h2 className="text-xl font-semibold mb-2">Download NonMouse</h2>
                <p className="text-muted-foreground mb-4">
                  You can download the latest available builds and source code from GitHub Releases.
                </p>
                <a href="https://github.com/takeyamayuki/NonMouse/releases" target="_blank" rel="noopener noreferrer">
                  <Button>
                    <Download className="mr-2 h-4 w-4" />
                    Open GitHub Releases
                  </Button>
                </a>
              </div>

              <div className="rounded-2xl bg-accent p-5">
                <h2 className="text-xl font-semibold mb-2">Support / early-access updates</h2>
                <p className="text-muted-foreground mb-4">
                  If you need setup help or have questions about your supporter purchase, contact us with the email address used at checkout.
                </p>
                <a href="mailto:kintre.ndy0@gmail.com?subject=NonMouse%20Early%20Access%20Support">
                  <Button variant="secondary">
                    <Mail className="mr-2 h-4 w-4" />
                    Contact support
                  </Button>
                </a>
              </div>
            </div>

            <div className="flex flex-wrap gap-3">
              <Link href="/">
                <Button variant="outline">
                  <ArrowLeft className="mr-2 h-4 w-4" />
                  Back to NonMouse
                </Button>
              </Link>
              <a href="https://github.com/takeyamayuki/NonMouse" target="_blank" rel="noopener noreferrer">
                <Button variant="outline">
                  <Github className="mr-2 h-4 w-4" />
                  View source on GitHub
                </Button>
              </a>
            </div>
          </div>
        </div>
      </section>
    </main>
  );
}
