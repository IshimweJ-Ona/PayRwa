# PayRwa - [Your Name]

A web application for seamless mobile payments, currency exchange, and QR code transactions in Rwanda.

## Features

- **User Registration & Login:** Secure authentication with password hashing.
- **Mobile Money Payments:** Integrates with MTN MoMo API for real-time payments.
- **Currency Exchange:** Converts between supported currencies.
- **QR Code Payments:** Scan and generate QR codes for transactions.
- **Transaction History:** View all your payment history.
- **Responsive Frontend:** Modern UI with mobile support.

## Technologies Used

- **Backend:** Python, Flask, MySQL, dotenv
- **Frontend:** HTML, CSS, JavaScript (Vanilla)
- **APIs:** MTN MoMo (sandbox), Currency Exchange API
- **Other:** Jinja2, Flask-Login, Flask-CORS

## Folder Structure

```
PayRwa/
├── backend/
│   ├── app/
│   └── create-table-template.sql
├── frontend/
│   ├── static/
│   └── templates/
├── requirements.txt
├── .env.example
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/payrwa-yourname.git
   cd payrwa-yourname
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   - Copy `.env.example` to `.env` and fill in your credentials (MySQL, MTN MoMo, etc.).

4. **Set up the database:**
   - Create a MySQL database (locally or on a cloud provider).
   - Import `backend/create-table-template.sql` using phpMyAdmin or MySQL Workbench.

5. **Run the app locally:**
   ```sh
   python backend/app/__init__.py
   ```
   *(Or your main entry point)*

6. **Deploy to Render/Railway:**
   - Push your code to GitHub.
   - Follow Render/Railway instructions for Python/Flask deployment.
   - Add your environment variables in the dashboard.

## Environment Variables

See `.env.example` for required variables:
```
DB_HOST=
DB_USER=
DB_PASSWORD=
DB_NAME=
MOMO_PRIMARY_KEY=
MOMO_SECONDARY_KEY=
MOMO_API_USER=
MOMO_API_KEY=
MOMO_CALLBACK_URL=
APP_SECRET_KEY=
```

## Assignment Customization

- All URLs and naming conventions use your name.
- HTTPS is enabled via Render/Railway.
- All assignment requirements are met.

## License

This project is for educational purposes.

---

**For any issues, contact [your.email@domain.com].**