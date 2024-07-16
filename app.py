import streamlit as st



col1, col2 = st.columns(2)


with col1:
    st.header("Input Question")
    question = st.text_area("Enter your question here:", height=270)
    with st.expander("Actor Settings", expanded=False):
        # Create file uploader for Actor Face Image
        face_image = st.file_uploader("Actor Face Image", type=["png", "jpg", "jpeg"], key='face_image',
                                      help='Limit 200MB per file')

        # Create file uploader for Actor Composition
        composition = st.file_uploader("Actor Composition", type=["png", "jpg", "jpeg"], key='composition',
                                       help='Limit 200MB per file')

        # Create file uploader for Actor Style
        style = st.file_uploader("Actor Style", type=["png", "jpg", "jpeg"], key='style',
                                 help='Limit 200MB per file')

    with st.expander("Video Settings", expanded=False):
        pass
    if st.button("Generate Answer"):
        pass


with col2:
    st.header("Generated Answer")
    answer = st.text_area("Answer:", value=st.session_state.get('generated_answer', ''), height=550)
    if st.button("Generate Video"):
      st.write("Generating video...")



# Display the generated answer if any
if 'generated_answer' in st.session_state:
    st.write(st.session_state.generated_answer)


