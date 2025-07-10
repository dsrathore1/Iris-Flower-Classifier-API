"use client"

import { useEffect, useState } from "react"

export default function Test() {
    const [response, setResponse] = useState();

    useEffect(() => {
        const sendData = async () => {
            try {
                const res = await fetch("http://localhost:8000/api/test", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        name: "AutoUser",
                        msg: "This msg was sent from useEffect!"
                    }) || "Loading ..."
                });
                const data = await res.json()
                setResponse(data.message)
            } catch (err) {
                console.error("Failed to POST :", err)
                setResponse("Failed to send Message")
            }
            sendData()
        }
    }, [])
    return (
        <>
            <div className="h-screen bg-grey-800 flex items-center justify-center flex-col gap-10">
                <h1 className="text-5xl uppercase">Auto POST with useEffect</h1>
                <h2 className="text-3xl uppercase">Response from API 👇🏻</h2>
                <p>{response || "Sending ..."}</p>
            </div>
        </>
    );
}