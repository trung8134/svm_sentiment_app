import streamlit as st
import joblib
# from underthesea import word_tokenize
import spacy
import string

def load_model():
    # Thay đổi đường dẫn đến file .sav của bạn
    with open('DEMO+CODE/Deploy_web/svm_model.joblib', 'rb') as f:
        model = joblib.load(f)
    return model
def load_lsa() :
    with open('DEMO+CODE/Deploy_web/lsa_pipeline.joblib', 'rb') as f:
        lsa = joblib.load(f)
    return lsa

def load_vectorizer():
    with open('DEMO+CODE/Deploy_web/tfidf_vectorizer.joblib', 'rb') as f:
        tfidf = joblib.load(f)
    return tfidf


# Tải model khi ứng dụng bắt đầu
model = load_model()
tfidf = load_vectorizer()
lsa = load_lsa() 

def pre_process(text):
  nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
  # lower()
  text = text.lower()
  doc = nlp(text)
  # tokens
  # check punct
  tokens = [token.text for token in doc if token.text not in string.punctuation]
  return ' '.join(tokens)


def processed_input(text):
    text = pre_process(text)
    text_tfidf = tfidf.transform([text])
    input_txt = lsa.transform(text_tfidf)
    return input_txt

def main():

    st.title('DỰ ĐOÁN CẢM XÚC CỦA SINH VIÊN KHI THAM GIA MÔN CÁC PHƯƠNG PHÁP HỌC THỐNG KÊ')
    st.markdown('Chào mừng đến với ứng dụng của nhóm THHD')

    
    text = st.text_input('Nhập phản hồi của bạn tại đây:', "")

    if (st.button('Dự đoán') and st.text_input):
        input = processed_input(text)
        # Sử dụng model để dự đoán
        with st.spinner('Đang dự đoán...'):
            prediction = model.predict(input)
            st.success('Successful!', icon="✅")
            st.write('Kết quả dự đoán:')
            if (prediction[0] == 0):
                st.write("Học sinh có cảm xúc tiêu cực đối với môn học này")
            elif  (prediction[0] == 1):
                st.write("Học sinh có cảm xúc bình thường đối với môn học này")
            else:
                st.write("Học sinh có cảm xúc tích cực đối với môn học này")
                
if __name__ == '__main__':
    main()

