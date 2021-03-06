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

![alt text](https://github.com/avinashpaul2012/GAN-endoscopy-classification/blob/main/GAN%20diagram.png)

Endoscopic polyps are classified using a modified GAN architecture. A standard classifier using
GAN takes a data point, x as input for classifying it into K classes. This is done by introducing
a softmax function at the output layer for supervised learning problems. This can be converted
into a semi-supervised problem by simply adding an extra class and increasing the dimension of
our network to K+1.

In semi-supervised learning, the GAN is trained on a limited labeled endoscopic dataset and
from many unlabeled endoscopic images. The architecture Discriminator D and Generator G
is changed. D in our method works on two modes. In the supervised mode, D trains on the
labeled (x,y) pair, while in the unsupervised mode, GAN mimics the classical GAN model taking
x as input and doing the task of classifying polyps as real or fake. The discriminator in semisupervised
mode is trained using two independent models that share the network parameters. In
the unsupervised mode, the output of the discriminator is a softmax function with K classes of
polyps.
