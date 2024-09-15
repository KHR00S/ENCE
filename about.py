import streamlit as st
from st_social_media_links import SocialMediaIcons


def app():

    # Language selection
    lang = st.selectbox("Select Language / Pilih Bahasa", ["Bahasa Indonesia", "English"])

    if lang == "Bahasa Indonesia":
        # Indonesian content
        st.title("Dashboard Prediksi Kebakaran Melalui Citra Gambar")
        st.markdown("Selamat datang di Dashboard Prediksi Kebakaran Melalui Citra Gambar! Dashboard ini dirancang untuk membantu dalam mendeteksi potensi kebakaran hutan dan lahan secara cepat dan akurat melalui analisis citra gambar. Menggunakan teknologi pembelajaran mesin dan pemrosesan gambar, sistem ini mampu mengidentifikasi area berisiko tinggi berdasarkan data visual yang diunggah.")
        st.header("Deskripsi Projek")
        st.markdown("""
            Pembuatan dashboard ini merupakan salah satu luaran dari Big Data Competition Statistics Explore 2024 yang dikerjakan oleh Mahasiswa Universitas Syiah Kuala.
        """)
        st.image('Picture1.png', use_column_width=True)

        col_1, col_2, col_3 = st.columns(3)
        with col_1:
            st.header("Visi")
            st.markdown("""
            Menjadi penyedia solusi inovatif dalam mendeteksi potensi kebakaran hutan dan lahan melalui analisis citra gambar yang akurat untuk mendukung upaya mitigasi kebakaran secara efektif.
            """)
        with col_2:
            st.header("Misi")
            st.markdown("""
            1. Mengumpulkan dan menganalisis data citra gambar terkait potensi kebakaran hutan dan lahan secara akurat.
            2. Mengembangkan model prediksi kebakaran yang andal dengan menggunakan teknologi pembelajaran mesin dan data visual.
            3. Menyediakan dashboard interaktif yang memudahkan pemantauan dan peringatan dini risiko kebakaran.
            4. Menyebarkan informasi terkait risiko kebakaran hutan dan lahan kepada pihak-pihak terkait secara cepat dan efektif.
            """)
        with col_3:
            st.header("Tujuan")
            st.markdown("""
            1. Menyediakan sumber informasi yang terpercaya mengenai potensi kebakaran hutan dan lahan.
            2. Meningkatkan kewaspadaan dan kesiapsiagaan masyarakat serta pemangku kepentingan terhadap risiko kebakaran.
            3. Mendukung upaya mitigasi dan penanggulangan kebakaran hutan dan lahan di Indonesia.
            """)

        st.header("Dataset yang Digunakan")
        st.markdown("""
            Kami menggunakan dataset citra gambar [kaggle](https://www.kaggle.com/competitions/big-data-competition-statistics-explore-2024/overview) dengan kelas:
        """)
        st.image('Picture2.png', use_column_width=True)

        col_1, col_2, col_3, col_4 = st.columns(4)
        with col_1:
            st.header("Fire")
            st.markdown("""
            Menampilkan dominan keberadaan api.
            """)
        with col_2:
            st.header("None")
            st.markdown("""
            Tidak menunjukkan adanya tanda-tanda kebakaran atau asap.
            """)
        with col_3:
            st.header("Smoke")
            st.markdown("""
            Menunjukkan dominan adanya asap.
            """)
        with col_4:
            st.header("Smoke and Fire")
            st.markdown("""
            Menunjukkan keberadaan api dan asap secara bersamaan.
            """)

        st.header("Teknologi / Tools yang Digunakan")
        st.markdown("""
            - **Streamlit:** Untuk pembuatan antarmuka pengguna.
            - **Pandas:** Untuk manipulasi dan analisis data.
            - **Onnxruntime:** Untuk menyimpan dan memuat model pembelajaran mesin.
        """)

        st.header("Kontak")
        st.markdown("""
            Jika Anda memiliki pertanyaan atau umpan balik, silakan hubungi kami:
        """)
        col_4, col_5 = st.columns(2)
        with col_4:
            st.markdown("""
                - **Muhammad Zia Ulhaq**
                    - Email: [ziaswatfbicia@gmail.com](mailto:ziaswatfbicia@gmail.com) 
                    - LinkedIn: [Muhammad Zia Ulhaq](https://www.linkedin.com/in/muhammad-zia-ulhaq-8373112b9/) 
            """)
        with col_5:
            st.markdown("""
                - **Fakhrus Syakir**
                    - Email: [fakhroosyakir@gmail.com](mailto:fakhroosyakir@gmail.com) 
                    - LinkedIn: [Fakhrus Syakir](https://www.linkedin.com/in/fakhrus-syakir-65bb72205/) 
            """)

    else:
        # English content
        st.title("Forest Fire Prediction Dashboard Through Image Analysis")
        st.markdown("Welcome to the Fire Prediction Dashboard through Imagery! This dashboard is designed to assist in detecting potential forest and land fires quickly and accurately through image analysis. Using machine learning and image processing technologies, the system is able to identify high-risk areas based on uploaded visual data.")
        st.header("Project Description")
        st.markdown("""
            This dashboard is one of the outputs from the Big Data Competition Statistics Explore 2024, created by students of Syiah Kuala University.
        """)
        st.image('Picture1.png', use_column_width=True)

        col_1, col_2, col_3 = st.columns(3)
        with col_1:
            st.header("Vision")
            st.markdown("""
            To be an innovative solution provider in detecting forest and land fire potential through accurate image analysis to support effective fire mitigation efforts.
            """)
        with col_2:
            st.header("Mission")
            st.markdown("""
            1. Accurately collect and analyze image data related to forest and land fire potential.
            2. Develop reliable fire prediction models using machine learning and visual data technologies.
            3. Provide an interactive dashboard to facilitate monitoring and early warning of fire risks.
            4. Disseminate fire risk information to relevant stakeholders quickly and effectively.
            """)
        with col_3:
            st.header("Goals")
            st.markdown("""
            1. Provide a trusted source of information on forest and land fire potential.
            2. Increase awareness and preparedness of the community and stakeholders against fire risks.
            3. Support mitigation and response efforts to forest and land fires in Indonesia.
            """)

        st.header("Datasets Used")
        st.markdown("""
            We use a dataset of image data from [Kaggle](https://www.kaggle.com/competitions/big-data-competition-statistics-explore-2024/overview) with the following classes:
        """)
        st.image('Picture2.png', use_column_width=True)

        col_1, col_2, col_3, col_4 = st.columns(4)
        with col_1:
            st.header("Fire")
            st.markdown("""
            Displays the dominance of fire presence.
            """)
        with col_2:
            st.header("None")
            st.markdown("""
            Does not show any signs of fire or smoke.
            """)
        with col_3:
            st.header("Smoke")
            st.markdown("""
            Shows the dominance of smoke presence.
            """)
        with col_4:
            st.header("Smoke and Fire")
            st.markdown("""
            Displays both fire and smoke presence.
            """)

        st.header("Technologies / Tools Used")
        st.markdown("""
            - **Streamlit:** For building the user interface.
            - **Pandas:** For data manipulation and analysis.
            - **Onnxruntime:** For saving and loading machine learning models.
        """)

        st.header("Contact")
        st.markdown("""
            If you have any questions or feedback, please contact us:
        """)
        col_4, col_5 = st.columns(2)
        with col_4:
            st.markdown("""
                - **Muhammad Zia Ulhaq**
                    - Email: [ziaswatfbicia@gmail.com](mailto:ziaswatfbicia@gmail.com) 
                    - LinkedIn: [Muhammad Zia Ulhaq](https://www.linkedin.com/in/muhammad-zia-ulhaq-8373112b9/) 
            """)
        with col_5:
            st.markdown("""
                - **Fakhrus Syakir**
                    - Email: [fakhroosyakir@gmail.com](mailto:fakhroosyakir@gmail.com) 
                    - LinkedIn: [Fakhrus Syakir](https://www.linkedin.com/in/fakhrus-syakir-65bb72205/) 
            """)
