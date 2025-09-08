# 🚨 Browser Autofill Data Leak PoC 🚨

This repository demonstrates how browser autofill can unintentionally leak sensitive personal data like address, phone number, and even payment details — even if a form only shows Name and Email fields.

⚠️ Disclaimer: This PoC is for educational and awareness purposes only. Do not use it for malicious activity.

## 🔎 How It Works

A user sees only Name and Email fields on the webpage.

Hidden fields (phone, address, city, state, zip, etc.) are embedded in the form.

Browser autofill silently fills those hidden fields.

When the form is submitted, all hidden data is sent to the server, not just the visible fields.

# 📺 Learn More

Medium post with explanation: https://achuappu.medium.com/f7f6ea6d5693
