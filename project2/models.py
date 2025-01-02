from transformers import  T5Tokenizer, T5ForConditionalGeneration

class ModelHandler:
    def __init__(self):
        self.translation_model_name = "google-t5/t5-base"
        self.translation_tokenizer = T5Tokenizer.from_pretrained(self.translation_model_name)
        self.translation_model = T5ForConditionalGeneration.from_pretrained(self.translation_model_name)

        self.summarization_model_name = "google-t5/t5-base"
        self.summarization_tokenizer = T5Tokenizer.from_pretrained(self.summarization_model_name)
        self.summarization_model = T5ForConditionalGeneration.from_pretrained(self.summarization_model_name)

    def translate_text(self, text, source_lang="English", target_lang="German"):
        input_text = f"translate {source_lang} to {target_lang}: {text}"
        input_ids = self.translation_tokenizer(input_text, return_tensors="pt").input_ids
        
        outputs = self.translation_model.generate(input_ids, max_length=100, num_beams=4, early_stopping=True)
        translated_text = self.translation_tokenizer.decode(outputs[0], skip_special_tokens=True)
        return translated_text

    def summarize_text(self, text, max_length=50, min_length=10):
        input_text = f"summarize: {text}"
        input_ids = self.summarization_tokenizer(input_text, return_tensors="pt").input_ids
        
        outputs = self.summarization_model.generate(input_ids, max_length=max_length, min_length=min_length, num_beams=4, early_stopping=True)
        summary = self.summarization_tokenizer.decode(outputs[0], skip_special_tokens=True)
        return summary