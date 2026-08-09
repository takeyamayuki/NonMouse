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
          <div className="flex space-x-4">
            <a
              href="https://github.com/takeyamayuki/NonMouse"
              target="_blank"
              rel="noopener noreferrer"
              className="text-muted-foreground hover:text-primary"
            >
              <Github className="w-5 h-5" />
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
}