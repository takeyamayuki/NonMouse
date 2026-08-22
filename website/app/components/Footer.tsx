import { Github } from "lucide-react";

export function Footer() {
  return (
    <footer className="bg-background border-t">
      <div className="container px-4 py-8 mx-auto">
        <div className="flex flex-col md:flex-row justify-between items-center">
          <div className="mb-4 md:mb-0">
            <p className="text-sm text-muted-foreground">
              © 2025 NonMouse. All rights reserved.
            </p>
          </div>
          <div className="flex flex-wrap items-center justify-center gap-x-4 gap-y-2 text-sm text-muted-foreground">
            <a href="/terms" className="hover:text-primary">Terms</a>
            <a href="/privacy" className="hover:text-primary">Privacy</a>
            <a href="/legal" className="hover:text-primary">Commerce Disclosure</a>
            <a href="/contact" className="hover:text-primary">Contact</a>
            <a
              href="https://github.com/takeyamayuki/NonMouse"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:text-primary"
              aria-label="NonMouse on GitHub"
            >
              <Github className="w-5 h-5" />
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
}