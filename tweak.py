#!/usr/bin/env python
# coding: utf-8

# In[3]:


from keras.datasets import mnist


# In[2]:


dataset=mnist.load_data('mymnist.db')


# In[3]:


len(dataset)


# In[4]:


train , test = dataset


# In[5]:


len(train)


# In[6]:


X_train , y_train = train


# In[7]:


X_train.shape


# In[8]:


X_test, y_test = test


# In[9]:


X_test.shape


# In[10]:


img1 = X_train[0]


# In[11]:


img1


# In[12]:


img1.shape


# In[13]:


img1_label=y_train[0]


# In[14]:


img1_label


# In[15]:




# In[17]:


img_label= y_train[5]


# In[18]:


img1d=img1.reshape(28*28)


# In[19]:


img1d.shape


# In[20]:


X_train.shape


# In[21]:


X_train_1d = X_train.reshape(-1 , 28*28)


# In[22]:


X_train = X_train_1d.astype('float32')


# In[23]:


y_train.shape


# In[24]:


from keras.utils.np_utils import to_categorical


# In[25]:


y_train_cat=to_categorical(y_train)


# In[26]:


y_train_cat


# In[27]:


from keras.models import Sequential


# In[28]:


from keras.layers import Dense


# In[29]:


model =Sequential()


# In[30]:
model.add(Dense(units=512, input_dim = 28*28, activation= 'relu'))
model.add(Dense(units=256, activation='relu'))
i=1
for i in range(i):
    model.add(Dense(units=128,activation='relu'))
    
model.add(Dense(units=10, activation='softmax'))
model.summary()
from keras.optimizers import RMSprop


# In[39]:


model.compile(optimizer= RMSprop(),loss='categorical_crossentropy', metrics=['accuracy'])


# In[40]:


h = model.fit(X_train, y_train_cat,epochs=5)


# In[46]:


X_test_1d=X_test.reshape(-1, 28*28)


# In[47]:


X_test= X_train_1d.astype('float32')


# In[48]:


y_test_cat=to_categorical(y_test)


# In[49]:


model.predict(X_test)


# In[50]:


y_test_cat


# In[50]:

p=h.history['accuracy']
h.history['accuracy'][4]


# In[51]:

with open('file.txt', 'w') as f:
    f.write(str(p[4]))

model.save('mymodel.h1')
curl -u admin:redhat 192.168.43.135:8080/job/taskjob3/build?token=redhat