import { useEffect } from "react";
import { AppProps } from "next/app";
import "../app/globals.css";

function IdzDoParku({ Component, pageProps }: AppProps) {
  useEffect(() => {
    const handleUnload = async () => {
      const sessionId = sessionStorage.getItem("session_id");
      if (!sessionId) return;

      try {
        await fetch("http://localhost:8000/api/logout/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ session_id: sessionId }),
        });
        sessionStorage.removeItem("session_id");
      } catch (error) {
        console.error("Logout error:", error);
      }
    };

    window.addEventListener("beforeunload", handleUnload);

    return () => {
      window.removeEventListener("beforeunload", handleUnload);
    };
  }, []);

  return <Component {...pageProps} />;
}

export default IdzDoParku;
