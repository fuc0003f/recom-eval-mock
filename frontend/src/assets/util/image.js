export function getImgUrl(brand) {
  var images = require.context("../../assets/logos/", false, /\.png$/);
  return images("./" + brand + ".png");
}
