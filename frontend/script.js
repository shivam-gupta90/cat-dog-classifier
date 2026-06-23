async function predictImage(){

    const fileInput =
        document.getElementById(
            "imageInput"
        );

    const file =
        fileInput.files[0];

    if(!file){

        alert(
            "Select image first"
        );

        return;
    }

    const formData =
        new FormData();

    formData.append(
        "file",
        file
    );

    const response =
        await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method:"POST",
                body:formData
            }
        );

    const data =
        await response.json();

    document.getElementById(
        "result"
    ).innerHTML =

        `Prediction :
        ${data.prediction}
        <br>
        Confidence :
        ${data.confidence}%`;
}