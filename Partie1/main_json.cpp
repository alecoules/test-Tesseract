#include <leptonica/allheaders.h>
#include <tesseract/baseapi.h>
#include <fstream>
#include <string>
#include <iostream>
#include <json/writer.h>

int main()
{
  Pix *image = pixRead("01_alb_id.tif");
  tesseract::TessBaseAPI *api = new tesseract::TessBaseAPI();
  api->Init(NULL, "eng");
  api->SetImage(image);
  
  //obtention des boxes
  Boxa* boxes = api->GetComponentImages(tesseract::RIL_TEXTLINE, true, NULL, NULL);
  printf("Found %d textline image components.\n", boxes->n);

  //On ecrit le json ligne à ligne 
  //dans une boucle for
  Json::Value result;   

  for (int i = 0; i < boxes->n; i++) {
    BOX* box = boxaGetBox(boxes, i, L_CLONE);
    api->SetRectangle(box->x, box->y, box->w, box->h);
    char* ocrResult = api->GetUTF8Text();
    int conf = api->MeanTextConf();
    result["boxes"][std::to_string(i)]["x"] = box->x;
    result["boxes"][std::to_string(i)]["y"] = box->y;
    result["boxes"][std::to_string(i)]["w"] = box->w;
    result["boxes"][std::to_string(i)]["h"] = box->h;
    result["boxes"][std::to_string(i)]["text"] = ocrResult;
    result["boxes"][std::to_string(i)]["confidence"] = conf;
  }

  std::ofstream file("output.json");
  file << result;

}
