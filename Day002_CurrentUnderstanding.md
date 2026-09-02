# Day 02 — Mental Model v1

## How does one model compare an image and a sentence?

As per my current understanding of text-to-image or image-to-text models, the basic idea is that both inputs can be converted into vector embeddings. The input can be an image or text, and the model converts each of them into numerical representations called embeddings.

After getting these embeddings, I think they are placed into some kind of vector space. The important idea seems to be that an image and a sentence that have similar meanings should be closer to each other in this vector space. For example, if I have an image of a person wearing spectacles and the sentence is "a person wearing spectacles", I expect their embeddings to be more similar than the image embedding and a sentence such as "a car driving on a highway".

The similarity between the image and text can then be calculated. I currently think cosine similarity is used to measure how similar the two vectors are. If the vectors point in similar directions, the cosine similarity should be high. If they point in very different directions, it should be lower. Therefore, the text label with the highest similarity score should be the label that the model considers the best match for the image.

I also understand that the similarity scores can be converted into probabilities using softmax. This is what I observed in my CLIP experiment. I gave one image and eight labels, and CLIP produced a probability for each label. The probabilities added up to approximately one. The label "a person wearing spectacles" received the highest probability in my experiment.

However, I do not have a complete understanding of how this actually happens inside the model. I am not sure whether the image and text embeddings are literally put into one common vector space or whether there is another mechanism that makes them comparable. I also don't understand how the raw image and sentence are converted into embeddings in the first place.

I currently think there must be some neural network process that takes the image pixels and produces an image vector, while another process takes the words and produces a text vector. Somehow these two processes must be trained so that related images and sentences produce embeddings that are close or have high similarity.

My CLIP experiment showed me that the wording also matters. When I changed "a person wearing spectacles" to "a person wearing glasses", the similarity score changed even though the two phrases mean almost the same thing to me. This makes me think that the text representation is sensitive to the exact wording.

I currently understand the overall pipeline as:

raw image + sentence → embeddings → vector representation → similarity calculation → scores → softmax probabilities.

But most of the middle of this pipeline is still unclear to me. I know the basic idea of vectors and cosine similarity, but I do not yet understand how a neural network learns to create useful image and text embeddings or how the two different types of information become comparable.

## Five things I do NOT understand

1. I do not understand how image and text embeddings are put into a common vector space so that their similarity can be measured.

2. I do not understand how text is converted into an embedding vector.

3. I do not understand how an image is converted into an embedding vector.

4. I understand vectors, but I do not yet understand exactly what a tensor is and why deep-learning models use tensors.

5. I do not understand the architecture of CLIP or exactly what happens inside its image and text components.

## Three falsifiable predictions

1. If I give CLIP an image containing an object or concept that is very different from anything represented in its training data, its classification should become unreliable and its highest-scoring label may be essentially arbitrary.

2. If I use labels that describe things that are difficult to determine from the image itself, such as a person's private intention or the exact reason they are doing something, CLIP should perform poorly compared with labels describing visible objects or scenes.

3. If I change the wording of a label while keeping its general meaning similar, the similarity score should change because CLIP's text representation depends on the exact words and phrasing.

## Self-check

The most fundamental unknown for me is probably **how image and text embeddings become comparable in the first place**. I understand that both become vectors, but I do not yet understand how two completely different types of input—pixels and language—can end up in a representation where their similarity has meaning.
