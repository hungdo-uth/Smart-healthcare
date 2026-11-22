
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Smart Healthcare",
    page_icon="❤️",
    layout="wide"
)

st.title("❤️ SMART HEALTHCARE")
st.subheader("Ứng dụng hỗ trợ theo dõi sức khỏe thông minh")

st.info(
    "Ứng dụng chỉ cung cấp thông tin tham khảo, "
    "không thay thế chẩn đoán của bác sĩ."
)

# Cơ sở dữ liệu
data = {
    "Benh": [
        "Cảm lạnh thông thường",
        "Cúm",
        "Viêm họng",
        "Viêm mũi dị ứng",
        "Viêm xoang",
        "Đau đầu",
        "Đau nửa đầu",
        "Viêm phế quản cấp",
        "Hen suyễn",
        "Rối loạn tiêu hóa",
        "Viêm dạ dày",
        "Tiêu chảy cấp",
        "Táo bón",
        "Nhiễm trùng đường tiết niệu",
        "Đau cơ"
    ],
    "Trieu_chung": [
        ["ho", "sổ mũi", "hắt hơi"],
        ["sốt", "ho", "đau đầu", "đau cơ"],
        ["đau họng", "nuốt đau", "sốt"],
        ["hắt hơi", "ngứa mũi", "sổ mũi"],
        ["đau đầu", "nghẹt mũi", "đau mặt"],
        ["đau đầu"],
        ["đau đầu", "buồn nôn", "nhạy cảm ánh sáng"],
        ["ho", "đờm", "đau ngực"],
        ["khó thở", "khò khè", "tức ngực"],
        ["đau bụng", "đầy hơi", "buồn nôn"],
        ["đau bụng", "buồn nôn", "ợ nóng"],
        ["tiêu chảy", "đau bụng", "buồn nôn"],
        ["táo bón", "đầy bụng", "đau bụng"],
        ["tiểu buốt", "tiểu nhiều", "đau bụng dưới"],
        ["đau cơ", "mỏi cơ"]
    ],
    "Loi_khuyen": [
        "Nghỉ ngơi, uống đủ nước và theo dõi triệu chứng.",
        "Nghỉ ngơi, uống đủ nước và theo dõi diễn biến sốt.",
        "Nghỉ ngơi và theo dõi đau họng.",
        "Hạn chế tiếp xúc tác nhân gây dị ứng.",
        "Theo dõi nghẹt mũi và đau vùng mặt.",
        "Nghỉ ngơi và theo dõi mức độ đau đầu.",
        "Nghỉ ngơi ở nơi yên tĩnh và theo dõi triệu chứng.",
        "Tránh khói thuốc và theo dõi tình trạng ho.",
        "Tránh tác nhân kích phát, thực hiện kế hoạch điều trị của bác sĩ.",
        "Ăn uống phù hợp và theo dõi tiêu hóa.",
        "Ăn uống điều độ và theo dõi triệu chứng.",
        "Bù nước và điện giải phù hợp.",
        "Tăng chất xơ và uống đủ nước nếu phù hợp.",
        "Nên được nhân viên y tế đánh giá.",
        "Nghỉ ngơi và tránh vận động quá sức."
    ]
}

df = pd.DataFrame(data)

# Danh sách triệu chứng
danh_sach = sorted(set(
    symptom
    for symptoms in df["Trieu_chung"]
    for symptom in symptoms
))

# Thông tin người dùng
st.header("1. Thông tin người sử dụng")

col1, col2 = st.columns(2)

with col1:
    tuoi = st.number_input(
        "Tuổi",
        min_value=0,
        max_value=120,
        value=20
    )

with col2:
    gioi_tinh = st.selectbox(
        "Giới tính",
        ["Nam", "Nữ", "Khác", "Không muốn trả lời"]
    )

# Triệu chứng
st.header("2. Nhập triệu chứng")

trieu_chung = st.multiselect(
    "Bạn đang gặp những triệu chứng nào?",
    danh_sach,
    placeholder="Chọn một hoặc nhiều triệu chứng"
)

so_ngay = st.number_input(
    "Triệu chứng xuất hiện bao nhiêu ngày?",
    min_value=0,
    max_value=365,
    value=1
)

# Dấu hiệu nguy hiểm
st.header("3. Kiểm tra dấu hiệu cảnh báo")

dau_hieu_nguy_hiem = st.multiselect(
    "Bạn có gặp dấu hiệu nào dưới đây không?",
    [
        "Khó thở nghiêm trọng",
        "Đau ngực dữ dội",
        "Ngất hoặc mất ý thức",
        "Co giật",
        "Lú lẫn đột ngột",
        "Yếu liệt đột ngột một bên cơ thể",
        "Đau đầu đột ngột dữ dội bất thường"
    ]
)

# Phân tích
st.header("4. Phân tích sức khỏe")

if st.button("🔍 PHÂN TÍCH TRIỆU CHỨNG"):

    if dau_hieu_nguy_hiem:

        st.error(
            "CẢNH BÁO: Bạn đã chọn dấu hiệu có thể nghiêm trọng. "
            "Hãy liên hệ cấp cứu hoặc đến cơ sở y tế ngay. "
            "Không chờ kết quả phân tích của ứng dụng."
        )

    elif not trieu_chung:

        st.warning("Vui lòng chọn ít nhất một triệu chứng.")

    else:

        ket_qua = []

        for _, row in df.iterrows():

            trung_khop = set(trieu_chung) & set(row["Trieu_chung"])

            if trung_khop:

                ket_qua.append({
                    "Bệnh lý tham khảo": row["Benh"],
                    "Số triệu chứng trùng": len(trung_khop),
                    "Triệu chứng trùng": ", ".join(
                        sorted(trung_khop)
                    ),
                    "Lời khuyên": row["Loi_khuyen"]
                })

        ket_qua = sorted(
            ket_qua,
            key=lambda x: x["Số triệu chứng trùng"],
            reverse=True
        )

        st.subheader("Kết quả tham khảo")

        st.write("Tuổi:", tuoi)
        st.write("Giới tính:", gioi_tinh)
        st.write("Thời gian có triệu chứng:", so_ngay, "ngày")

        if ket_qua:

            for item in ket_qua:

                with st.expander(
                    item["Bệnh lý tham khảo"]
                ):

                    st.write(
                        "Triệu chứng trùng:",
                        item["Triệu chứng trùng"]
                    )

                    st.write(
                        "Số triệu chứng trùng:",
                        item["Số triệu chứng trùng"]
                    )

                    st.write(
                        "Lời khuyên:",
                        item["Lời khuyên"]
                    )

        else:

            st.warning(
                "Không tìm thấy tình trạng tương đồng trong "
                "dữ liệu hiện có. Điều này không có nghĩa là "
                "bạn không mắc bệnh."
            )

        st.info(
            "Kết quả chỉ mang tính tham khảo. "
            "Nếu triệu chứng kéo dài, nặng lên hoặc khiến bạn "
            "lo lắng, hãy đến cơ sở y tế để được đánh giá."
        )

# Thông tin ứng dụng
st.divider()

st.caption(
    "SMART HEALTHCARE | Công cụ hỗ trợ tham khảo sức khỏe"
)
