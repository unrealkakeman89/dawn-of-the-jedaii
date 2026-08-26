#!/usr/bin/env python3
"""Minimal CORS static server for loading GMB markdown into browser preview."""

from __future__ import annotations

import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path


class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self) -> None:
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        super().end_headers()

    def do_OPTIONS(self) -> None:  # noqa: N802
        self.send_response(204)
        self.end_headers()


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--port", type=int, default=8765)
    p.add_argument("--directory", type=Path, required=True)
    args = p.parse_args()
    import os

    os.chdir(args.directory)
    HTTPServer(("127.0.0.1", args.port), CORSRequestHandler).serve_forever()


if __name__ == "__main__":
    main()
