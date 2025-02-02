
---

## **📌 AI Chatbot - Flask API**  
This is a simple **AI-powered chatbot** built using **Flask** and **Sentence Transformers**. It retrieves the most relevant answer based on user input using **semantic search**.

---

### **🔹 Features**  
✅ **Retrieval-Based AI** – Finds the best answer from a predefined Q&A dataset.  
✅ **Fast & Lightweight** – Works efficiently on **CPU** using `MiniLM`.  
✅ **Simple API** – Send a **question via POST request**, get an **AI response**.  

---

### **📌 How It Works**
1️⃣ **Loads a CSV file** containing **questions & answers**.  
2️⃣ Converts questions into **numerical embeddings** using `MiniLM`.  
3️⃣ **Finds the closest match** to the user’s question using **cosine similarity**.  
4️⃣ **Returns the best-matching answer** as JSON.  

---

### **🔹 Installation & Setup**
#### **1️⃣ Install Dependencies**
```bash
pip install torch transformers numpy pandas flask flask-cors
```

#### **2️⃣ Run the Flask API**
```bash
python chatbot.py
```

#### **3️⃣ Test API with cURL or Postman**
```bash
curl -X POST "http://127.0.0.1:5000/ask" -H "Content-Type: application/json" -d '{"question": "What is science?"}'
```

---

### **🔹 Frontend Integration**
Use the **`index.html`** file to interact with the chatbot via a simple **web interface**.

---

### **📌 Example API Response**
```json
{
    "answer": "Science is the systematic study of the natural world through observation and experimentation, aiming to uncover patterns and establish theories."
}
```

---

### **🔹 Next Steps**
✅ **Host the API online** (Render, AWS, etc.).  
✅ **Expand dataset** (add more Q&A).  
✅ **Fine-tune a model** for better accuracy.  

---

### **📌 Contributing**
Feel free to **modify & improve** this chatbot. If you have ideas, submit a **pull request**! 🚀🔥  

---
