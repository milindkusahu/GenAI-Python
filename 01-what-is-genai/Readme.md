# 🌐 Introduction to AI World

- **AI** predicts based on the **input** provided by the user.
- **OpenAI → GPT (Generative Pre-trained Transformer)**: A language model trained on vast text data.

### Types:

- **ChatGPT**: GPT + Tools/Agents → can access **real-time data** ✅
- **GPT API**: Pure model → **no real-time access** ❌

---

## ⚙️ Behind the Scenes – How it Works

### 🧠 Phase 1: Input and Encoding

1. **Input Query** → `"Man is to King as Woman is to ?"`
2. **Tokenization**: Converts words into numerical tokens for model processing  
   _Example_: `"Queen"` → `[5001]`
3. **Mathematics**: These tokens go through neural network layers.
4. **De-tokenization**: Numbers back to human-readable text.

🔗 **Try it**: [Tiktokenizer Tool](https://tiktokenizer.vercel.app/) – See how tokens map to words.

---

## 🔍 Vector Embeddings

- **Embeddings** represent words as **vectors** in multi-dimensional space.
- Similar meanings = Vectors close to each other.

### 📌 Example from Image:

```text
Man - Woman ≈ King - Queen
```

- This is a popular analogy visualized using **word vectors**.
- AI uses these **relationships** to understand context.

🧠 Think:  
If `"Man"` → `"King"`  
Then `"Woman"` → `"Queen"`

---

## 🧭 Positional Encoding

> Helps the model understand **word order** since transformers don't process tokens sequentially.

- Each word gets a **position-based encoding** added to its embedding.

### 🧪 Example:

```text
"The cat sat on the mat" ≠ "The mat sat on the cat"
```

Even with same words, **position changes meaning**, so token positions affect understanding.

---

## 🔄 Self-Attention Mechanism

> Allows the model to **weigh the importance** of other tokens when encoding a particular token.

🧠 Tokens "talk" to each other.

### 🧪 Example:

```text
"The river bank" → "bank" relates to water  
"The ICICI bank" → "bank" relates to finance
```

Self-attention uses **context** to resolve meaning.

---

## 🧪 Phase: Inferencing & Training

### 🔧 Training
1. Input: `<start> My name is Milind`
2. Output: model predicts next word → compares with actual → calculates **loss**
3. **Backpropagation** corrects weights.

```text
<start> My name is Milind → END  
     ↓  
Loss → Backprop → Adjust weights
```

### 🔄 Inference
1. Input token → Pass through layers
2. **Linear → Softmax → Probability distribution**
3. **Temperature** controls randomness in output:
   - `Low temp` (e.g. 0.2) → more predictable
   - `High temp` (e.g. 1.0) → more creative

---
