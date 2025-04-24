
# 📧 Email Classification with PII Masking API

## 🧩 Objective

The goal of this project is to build an **email classification system** for a company's support team. The system:
- Classifies incoming support emails into predefined categories.
- Masks personal and sensitive information (PII/PCI) **before processing**.
- Returns the classification result along with a **masked version of the email** and details of the masked entities.

---

## 🚀 Features

✅ **Email Classification**  
✅ **Regex-based PII Masking (No LLMs)**  
✅ **REST API using Flask**  
✅ **Strict JSON Output Format**

---

## 🧠 Problem Statement

You are to develop a solution that:
- Classifies emails (e.g., Billing Issues, Technical Support, etc.).
- Masks the following PII types before classification:
  - `full_name`
  - `email`
  - `phone_number`
  - `dob`
  - `aadhar_num`
  - `credit_debit_no`
  - `cvv_no`
  - `expiry_no`
- Provides a strict output structure as required.

---

## 🔧 Project Structure

```
.
├── app.py                  # Main script to run the API
├── api.py                  # Flask API endpoint
├── models.py               # Model training & loading logic
├── utils.py                # Text cleaning & PII masking
├── requirements.txt        # Python dependencies
├── model_pipeline.pkl      # Trained classification model
├── data/
│   └── combined_emails.csv # Training dataset
└── README.md               # This file
```

---

## ⚙️ Setup Instructions

1. **Clone the Repository**

```bash
git clone <your-repo-url>
cd <repo-directory>
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Train the Model**

```bash
python models.py
```

4. **Run the API**

```bash
python app.py
```

---

## 📬 API Usage

### 🔗 Endpoint

`POST /classify-email`

### 📥 Input JSON

```json
{
  "email": "Hello, my name is John Doe. You can contact me at johndoe@example.com or 9876543210."
}
```

### 📤 Output JSON

```json
{
  "input_email_body": "Hello, my name is John Doe. You can contact me at johndoe@example.com or 9876543210.",
  "list_of_masked_entities": [
    {
      "position": [18, 28],
      "classification": "full_name",
      "entity": "John Doe"
    },
    {
      "position": [56, 75],
      "classification": "email",
      "entity": "johndoe@example.com"
    },
    {
      "position": [79, 89],
      "classification": "phone_number",
      "entity": "9876543210"
    }
  ],
  "masked_email": "Hello, my name is [full_name]. You can contact me at [email] or [phone_number].",
  "category_of_the_email": "Technical Support"
}
```

---

## 🧪 Tools & Libraries Used

- **Python**: pandas, scikit-learn, joblib, Flask, regex
- **Model**: RandomForestClassifier
- **Text Processing**: Regex, custom masking logic
- **API**: Flask

---

## 🧾 Deliverables

- ✅ Python scripts for classification & PII masking
- ✅ Trained model file
- ✅ Flask API with `/classify-email` endpoint
- ✅ README with setup, usage, and strict API format
- ✅ Deployment ready for Hugging Face Spaces

---

## 📌 Evaluation Criteria

- ✅ API Deployment on Hugging Face Spaces
- ✅ Code Quality (PEP8 + Comments)
- ✅ Correct Masking & Output Format
- ✅ Working API with test cases

---

## 📎 Submission Format

- `app.py`
- `api.py`
- `models.py`
- `utils.py`
- `requirements.txt`
- `README.md`
- Trained model: `model_pipeline.pkl`


---

## 🔒 Example PII Masking

| Entity Type      | Example Input                     | Masked Output                  |
|------------------|-----------------------------------|--------------------------------|
| `full_name`      | John Doe                          | `[full_name]`                  |
| `email`          | johndoe@example.com               | `[email]`                      |
| `phone_number`   | 9876543210                        | `[phone_number]`               |
| `dob`            | 12/05/1992                        | `[dob]`                        |
| `aadhar_num`     | 1234-5678-9123                    | `[aadhar_num]`                 |
| `credit_debit_no`| 4111 1111 1111 1111               | `[credit_debit_no]`            |
| `cvv_no`         | 123                               | `[cvv_no]`                     |
| `expiry_no`      | 12/26                             | `[expiry_no]`                  |

---

## 📞 Contact

For any issues or improvements, feel free to open an issue or contribute to this repository!
