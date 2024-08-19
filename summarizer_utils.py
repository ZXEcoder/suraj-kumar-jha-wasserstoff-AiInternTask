from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_object_data(data):
    if len(data.strip()) > 20:
        summary = summarizer(data, max_length=50, min_length=25, do_sample=False)
        return summary[0]['summary_text']
    else:
        return "Text too short or not found"
