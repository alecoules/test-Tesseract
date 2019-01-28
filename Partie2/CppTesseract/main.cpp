#include <leptonica/allheaders.h>
#include <tesseract/baseapi.h>
#include <fstream>
#include <string>
#include <iostream>

int main()
{
    char *outText;

    tesseract::TessBaseAPI *api = new tesseract::TessBaseAPI();
    // Initialize tesseract-ocr with English, without specifying tessdata path
    if (api->Init(NULL, "eng")) {
        fprintf(stderr, "Could not initialize tesseract.\n");
        exit(1);
    }

    // Open input image with leptonica library
    Pix *image = pixRead("../01_alb_id.tif");
    api->SetImage(image);
    Pix *thresholded = api->GetThresholdedImage();
    pixWrite("../preprocessed_images/preprocess_tesseract.png", thresholded, IFF_PNG);
    // Get OCR result
    outText = api->GetUTF8Text();
    std::ofstream file("../text_outputs/output_1.txt");
    file << outText;

    // Destroy used object and release memory
    api->End();
    delete [] outText;
    pixDestroy(&image);

    return 0;
}
