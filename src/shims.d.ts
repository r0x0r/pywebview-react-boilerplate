declare global {
  interface PyWebview {
    state?: {
      setTicker?: (tick: string) => void;
    };
  }

  interface Window {
    pywebview?: PyWebview;
  }

  interface WindowEventMap {
    pywebviewready: unknown;
  }
}

export {};
