import tensorflow as tf

# Load dataset for MNIST

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

#scale the data so that RGB images are sclaed to matrices with max value of 1. 

x_train = x_train/255;
x_test  = x_test /255;

#Build a Keras Sequential Model. 

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)), 
    #First layer flattens a 28x28 2-D tensor to a 1x784 1-D tensor
    tf.keras.layers.Dense(128, activation='relu'), 
    #Second layer is a Dense layer with 128 neural units and ReLU activation. 
    tf.keras.layers.Dropout(0.2), 
    #A dropout layer with drop_probability=0.2
    tf.keras.layers.Dense(10) 
    # A Dense layer with 10 ouptuts, no activiation is specified so the default activation will be used
])

predictions = model(x_train[:1]).numpy()
#Apply first image from the training set to the NN model. Model is not yet trained.
#Node that numpy is an attibute of the model (not an attribute of the input data).

#print(predictions)

# use softmax to convert the 10 numbers in the predictions to a probabilty distribution for classes

#print(tf.nn.softmax(predictions).numpy)
#As per tutorial, the softmax layer should not be part of the mode to be trained because it can 
#impact the numerical stability of the training algorithm.

# now define a loss function for training the NN

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
#Use predifined loss function Sparse Categorial Cross Entropy 

# The loss function takes a vector of ground-truth values and a vector of logits and returns a scalar
#loss for each example.

#print(loss_fn(y_train[:1], predictions).numpy())

#Compile the model now and set the optimizer to 'adam' and loss to 'loss_fn'.

model.compile( optimizer='adam', loss=loss_fn, metrics=['accuracy'])
#use model.fit() to train the model on x_trin, y_train and define the training epochs

model.fit(x_train, y_train, epochs=5)

# Note that softmax layer was not the part of trained model. 
#Now evaluate the mode on x_test and y_test.
model.evaluate(x_test,y_test)

#Finally wrap this trained model into another model that has a softmax layer as its output. 

softmax_model = tf.keras.Sequential([
    model,
    #Use the pre-trained model as a block in the new model.
    tf.keras.layers.Softmax()
    #Add a softmax layer at the end.
    ])
softmax_model.compile( optimizer='adam', loss=loss_fn, metrics=['accuracy'])
softmax_model.evaluate(x_test, y_test)

