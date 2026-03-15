import streamlit as st
import pdf4llm
import pathlib

def main():  
    st.title("📄 extract pdf details in  txt")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"]) 

    if uploaded_file: 
        st.success(f"Uploaded: {uploaded_file.name}")
        proceed = st.button("Convert to txt") 

        if proceed:
            with st.spinner("Processing PDF..."):
                try:
                    temp_path = f"temp_{uploaded_file.name}" 
                    with open(temp_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                        
                    md_text = pdf4llm.to_markdown(temp_path)

                    # Save to output .md file
                    output_md_path = pathlib.Path("output.txt")
                    output_md_path.write_bytes(md_text.encode("utf-8"))

                    st.success("✅ Markdown extracted and saved as output.md")
                    st.download_button(
                        label="📥 Download ",
                        data=md_text,
                        file_name="output.txt",
                        mime="text/markdown"
                    )

                    st.markdown("---")
                    st.subheader("🔍 Preview:")
                    st.markdown(md_text)

                except Exception as e:
                    st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()


##extract pdf details and convert in txt format.


