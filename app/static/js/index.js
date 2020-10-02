let optionsDiv = null;
document.addEventListener("DOMContentLoaded", () => {
  document.querySelector("#optionsBtn").onclick = ToggleOptions;
  document.querySelector("#image").onchange = ShowImage;
  optionsDiv = document.querySelector("#options");
});

ToggleOptions = () => {
  if (optionsDiv.style.visibility == "visible") {
    optionsDiv.style.visibility = "hidden";
    optionsDiv.style.height = "0";
  } else {
    optionsDiv.style.visibility = "visible";
    optionsDiv.style.height = "14em";
  }
};

ShowImage = event => {
  let imageOutput = document.querySelector("#image-display");
  let img = event.target.files[0];
  imageOutput.src = URL.createObjectURL(img);
};
