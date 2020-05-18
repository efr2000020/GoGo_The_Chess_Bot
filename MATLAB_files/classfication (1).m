clear 
% webcamlist
% I = webcam(2);
outputfolder=fullfile('dataset'); %used to create file path
catergories={'bb','bk','bn','bp','bq','br','em','wb','wk','wn','wp','wq','wr'};  %pic foliders catergories
imds=imageDatastore(fullfile(outputfolder,catergories),'LabelSource','foldernames') %imds helps to mange the data (fullpath,lable to image)
tbl=countEachLabel(imds) % countig each label see how many image in each catigories 
minSetCount=min(tbl{:,2}) % finds the lowest number of pic in all categore pics----->tbl{:,2} find the lowest number i scond colum
imds=splitEachLabel(imds,minSetCount,'randomize'); % this function used to take the min number of the catogres where the pictures will be chosen randomized
countEachLabel(imds) % it count each label and show that they all have the same min number 
bb=find(imds.Labels=='bb',1) ;
bn=find(imds.Labels=='bn',1) ;
wb=find(imds.Labels=='wb',1) ;
bk=find(imds.Labels=='bk',1);
bp=find(imds.Labels=='bp',1) ;
bq=find(imds.Labels=='bq',1) ;
br=find(imds.Labels=='br',1) ;
wn=find(imds.Labels=='wn',1) ;
wk=find(imds.Labels=='wk',1);
wp=find(imds.Labels=='wp',1) ;
wq=find(imds.Labels=='wq',1) ;
wr=find(imds.Labels=='wr',1) ;
em=find(imds.Labels=='em',1);

net = resnet50();
net.Layers(1) % check the first layer size so we can size our pic to it 
net.Layers(end) %it shows how many classes to show many it can solve calassfication prornlems 
[trainingSet,testSet]=splitEachLabel(imds,0.2,'randomize') % it takes randomly  20 % images tb be trained and 70 % to be for tastung
imagesize=net.Layers(1).InputSize  ;       % take the size of the first layer so we can chnage our pic to this size 
argumentedTrainingset=augmentedImageDatastore(imagesize,trainingSet,'ColorPreprocessing','gray2rgb');   %control the size for the traingset and convert gray image to rgb 
argumentedTestset=augmentedImageDatastore(imagesize,testSet,'ColorPreprocessing','gray2rgb');   % do the same for testing images
w1=net.Layers(2).Weights;     %getting the weights of second layer
w1=mat2gray(w1) ; % it converts the wighted matrix to grayscale image
figure
montage(w1)       %shows the first convilution layers
title('First convolutional Layer weights')
featurelayer='fc1000';
trainingFeatures=activations(net,argumentedTrainingset,featurelayer,'miniBatchSize',32,'OutputAs','columns'); 
%using gpu memory and the activtion outputs shows as coulms
trainingLabels=trainingSet.Labels;
classifier=fitcecoc(trainingFeatures,trainingLabels,'Learner','Linear','Coding','onevsall','observationsIn','columns');  % (k(k-1)2 k---{ number of unit calss labels ( featuers , label) of traing set it return a trined model
testFeatures=activations(net,argumentedTestset,featurelayer,'miniBatchSize',32,'OutputAs','columns');
predictLabels=predict(classifier,testFeatures,'observationsIn','columns');  % it compare test features with training features
testslabels=testSet.Labels;
confMat=confusionmat(testSet.Labels,predictLabels);
confMat=bsxfun(@rdivide,confMat,sum(confMat,2)) % converted of conmat matric to persentage (1 means 100 %)
mean(diag(confMat)) % show the persentage the comparison betwwen tesated and trained pic
newImage=imread(fullfile('test (1).JPG'));
ds=augmentedImageDatastore(imagesize,newImage,'ColorPreprocessing','gray2rgb');
imagefeature=activations(net,ds,featurelayer,'miniBatchSize',32,'OutputAs','columns');
Label=predict(classifier,imagefeature,'observationsIn','columns')
sprintf('the loaded image belogs to %s class' , Label)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%I=imread(fullfile('test099.jpg'));  

%[m n k]=size(I)

%x= mat2cell(I,m/8*ones(8,1),n/8*ones(8,1),k)

h = figure
places=strings(8,8) ;
while ishandle(h)
    % Display and classify the image
    im = imread('orginal.jpg');
imm = imcrop(im,[140, 35, 485-20,475-10]);
  [m n k]=size(imm)

x= mat2cell(imm,m/8*ones(8,1),n/8*ones(8,1),k)

figure;
plotNumber = 1;
xlswrite('imageclassify.xlsx',places)
for i=1:size(x,1)
for j=1:size(x,2)
   subplot(8, 8, plotNumber);
  newImage=x{i,j};
ds=augmentedImageDatastore(imagesize,newImage,'ColorPreprocessing','gray2rgb');
imagefeature=activations(net,ds,featurelayer,'miniBatchSize',32,'OutputAs','columns');
Label=predict(classifier,imagefeature,'observationsIn','columns')
    imshow(x{i,j});
    
  
    str = sprintf('%s', Label);
    places(i+1,j)=str ;
      title(str);
    drawnow;
    if plotNumber == 1
      % Set up figure properties:
      % Enlarge figure to full screen.
      set(gcf, 'Units', 'Normalized', 'OuterPosition', [0 0 1 1]);
      % Get rid of tool bar and pulldown menus that are along top of figure.
      set(gcf, 'Toolbar', 'none', 'Menu', 'none');
      % Give a name to the title bar.
      set(gcf, 'Name', 'Demo by ImageAnalyst', 'NumberTitle', 'Off')
      hold on;
      drawnow;      
    end
    plotNumber = plotNumber + 1;
end
end 
end