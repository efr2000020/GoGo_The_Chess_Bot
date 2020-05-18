clear;
webcamlist
mycam = webcam(2);
img=imread("orginal.jpg")

if length(size(img))>2
img = rgb2gray(snapshot(mycam));

end 
figure 
imshow(img);
title('orginal image');
%%applying sobel edge detector in the horizontal direction
fx = [-1 0 1;-1 0 1;-1 0 1];
Ix = filter2(fx,img);
% applying sobel edge detector in the vertical direction
fy = [1 1 1;0 0 0;-1 -1 -1];
Iy = filter2(fy,img); 
Ix2 = Ix.^2;
Iy2 = Iy.^2;
Ixy = Ix.*Iy;
clear Ix;
clear Iy;
figure 
imshow(Ixy);
title('after applying sobel edge detector');
%applying gaussian filter on the computed value
h= fspecial('gaussian',[7 7],2); 
Ix2 = filter2(h,Ix2);
Iy2 = filter2(h,Iy2);
Ixy = filter2(h,Ixy);
height = size(img,1);
width = size(img,2);
result = zeros(height,width); 
R = zeros(height,width);
Rmax = 0;
figure 
imshow(Ixy);
title('after applying  gaussian filter 7*7');
for i = 1:height
for j = 1:width
M = [Ix2(i,j) Ixy(i,j);Ixy(i,j) Iy2(i,j)]; 
R(i,j) = det(M)-0.01*(trace(M))^2;
if R(i,j) > Rmax
Rmax = R(i,j);
end;
end;
end;
cnt = 0;
for i = 2:height-1
for j = 2:width-1
if R(i,j) > 0.1*Rmax && R(i,j) > R(i-1,j-1) && R(i,j) > R(i-1,j) && R(i,j) > R(i-1,j+1) && R(i,j) > R(i,j-1) && R(i,j) > R(i,j+1) && R(i,j) > R(i+1,j-1) && R(i,j) > R(i+1,j) && R(i,j) > R(i+1,j+1)
result(i,j) = 1;
cnt = cnt+1;
end;
end;
end;
[posc, posr] = find(result == 1);
cnt ;
figure
imshow(img);
title('After Harris Corner Detector  ')
hold on;
plot(posr,posc,'r.');
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Crop the image using corner detection and Dived the cropped image%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

imm = imcrop(im,[105, 10, 485-20,475-10]);
  [m n k]=size(imm)

x= mat2cell(imm,m/8*ones(8,1),n/8*ones(8,1),k)

figure;
plotNumber = 1;
for i=1:size(x,1)
for j=1:size(x,2)
   subplot(8, 8, plotNumber);
    newImage=x{i,j};
    imshow(x{i,j});
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


