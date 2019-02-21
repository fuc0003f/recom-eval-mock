// helper function to get the img url for a brand
export function getImgUrl(brand) {
  var images = require.context("../../assets/logos/", false, /\.png$/);
  return images("./" + brand + ".png");
}
