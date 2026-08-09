import { Header } from "./components/Header";
import { Hero } from "./components/Hero";
import { Features } from "./components/Features";
import { HowItWorks } from "./components/HowItWorks";
import { Demo } from "./components/Demo";
import { Testimonials } from "./components/Testimonials";
import { Download } from "./components/Download";
import { Footer } from "./components/Footer";

export default function Home() {
  return (
    <main>
      <Header />
      <Hero />
      <Features />
      <HowItWorks />
      <Demo />
      <Testimonials />
      <Download />
      <Footer />
    </main>
  );
}