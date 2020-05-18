clear
webcamlist
mycam = webcam(2);
x=rgb2gray(snapshot(mycam));
C = corner(x);
figure
imshow(x)
hold on
plot(C(:,1),C(:,2),'r*');
places=strings(8,8) 
figure

I2 = imcrop(x,[105, 10, 485-20,475-10]);


imshow(I2)
croppedImag = x(4:457, 30:480)
%imshow(croppedImag)
preview(mycam)