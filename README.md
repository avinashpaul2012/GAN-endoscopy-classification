Colon cancer is one of the leading causes of death in many parts of the world. It is caused due
to the occurrence of cancer cells called polyps in the intestinal tract. Colonic polyps have a very
high occurrence rate and can lead to cancer if left untreated. Polyps need to be detected before
they become cancerous. Endoscopic polyps can be classified into two main categories i.e. benign
and malignant. Classification is done mainly by expert physicians who annotate the polyp images.
This is however, time consuming and cumbersome to go through such large datasets of colonoscopy.
Here arises the need for automatic classification of polyps. Also, poor lighting and large inter class
variability adds to the problem of identifying the type of polyp.

Here I have implemented a GAN based data efficient classifier.The GAN based
classifier is a modified version of the classical GAN. In the modified architecture, the discriminator
is trained on supervised and unsupervised modes. Visual examination of polyps requires detail analysis by a skilled physician. Features like polyp
color, shape and texture vary greatly in polyps. Thus, colonoscopy data is both difficult to acquire
and annotating polyps is a cumbersome process. To address this issue of limited labeled data in endoscopic images, a semi-supervised classifier using generative adversarial network (GAN) is implemented here.

![alt text](http://url/to/img.png)
