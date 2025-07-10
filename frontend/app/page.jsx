"use client"
import { useEffect, useState } from "react"
import Link from "next/link";

export default function Home() {
  const [message, setMessage] = useState()

  useEffect(() => {
    fetch('http://127.0.0.1:8000')
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch((err) => console.error(err))
  }, []);

  return (
    <>
      <div className="h-screen bg-amber-400 flex items-center justify-center">
        <h1 className="uppercase h-[3rem] text-center text-4xl">{message}</h1>
      </div>
      <Link href="/test">
        Go To Test page
      </Link>
    </>
  );


}