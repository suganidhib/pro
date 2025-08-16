import React from "react";


export default function Home() {
  const token = localStorage.getItem("token");

  return (
    <div>
      <h2>Home Page</h2>
      <p>Welcome! 🎉</p>
      <p>Your token: {token}</p>
    </div>
  );
}
