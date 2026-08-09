import './globals.css';
import type { Metadata } from 'next';
import { Inter } from 'next/font/google';

const inter = Inter({ subsets: ['latin'] });
const gaMeasurementId = process.env.NEXT_PUBLIC_GA_MEASUREMENT_ID;

export const metadata: Metadata = {
  title: 'NonMouse - Control Your Computer with Hand Gestures',
  description: 'Transform your webcam into an intuitive mouse controller. Control your computer naturally with hand gestures using NonMouse.',
  keywords: ['hand gesture', 'mouse control', 'computer interface', 'webcam', 'accessibility'],
  authors: [{ name: 'NonMouse Team' }],
  openGraph: {
    title: 'NonMouse - Control Your Computer with Hand Gestures',
    description: 'Transform your webcam into an intuitive mouse controller.',
    images: ['https://i.gyazo.com/098d853fe184b677b10a9c0e7716484a.png'],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'NonMouse - Control Your Computer with Hand Gestures',
    description: 'Transform your webcam into an intuitive mouse controller.',
    images: ['https://i.gyazo.com/098d853fe184b677b10a9c0e7716484a.png'],
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        {gaMeasurementId ? (
          <>
            <script async src={`https://www.googletagmanager.com/gtag/js?id=${gaMeasurementId}`}></script>
            <script
              dangerouslySetInnerHTML={{
                __html: `
                  window.dataLayer = window.dataLayer || [];
                  function gtag(){dataLayer.push(arguments);}
                  gtag('js', new Date());
                  gtag('config', '${gaMeasurementId}');
                `,
              }}
            />
          </>
        ) : null}
        <link
          rel="icon"
          href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M16 8c0 2.21-1.79 4-4 4s-4-1.79-4-4 1.79-4 4-4 4 1.79 4 4z'/><path d='M12 14c-6.1 0-8 4-8 4v2h16v-2s-1.9-4-8-4z'/></svg>"
          type="image/svg+xml"
        />
      </head>
      <body className={inter.className}>{children}</body>
    </html>
  );
}