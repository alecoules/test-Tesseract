#include <leptonica/allheaders.h>
#include <tesseract/baseapi.h>
#include <fstream>
#include <string>
#include <iostream>

int main()
{
  Pix *image = pixRead("01_alb_id.tif");
  tesseract::TessBaseAPI *api = new tesseract::TessBaseAPI();
  api->Init(NULL, "eng");
  api->SetImage(image);

  //obtention de l'image preprocessee
  Pix *thresholded = api->GetThresholdedImage();
  //obtention des boxes
  Boxa *boxes = api->GetComponentImages(tesseract::RIL_SYMBOL, true, NULL, NULL);
  printf("Found %d textline image components.\n", boxes->n);

  //On dessine les boxes
  PIX * pix_boxes= pixDrawBoxa(thresholded, boxes,3,2);
  pixWrite("image_boxes_char.png", pix_boxes, IFF_PNG);

}
