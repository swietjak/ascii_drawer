document.addEventListener("DOMContentLoaded", () => {
  let text = document.querySelector("#result");
  let width = text.clientWidth;
  document.querySelector("#show-panel").style.width = toString(width) + " px";
  console.log(width);
});
