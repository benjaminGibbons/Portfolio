%Ben Gibbons Assignment 3
wghtd = [1 2 1; 2 4 2; 1 2 1];
stndrd = ones(5,5);
lapl = [1 1 1;1 -8 1;1 1 1];

Gx = [-1 0 1; -2 0 2; -1 0 1];
Gy = [1 2 1; 0 0 0; -1 -2 -1];


Circ = imread('Circuit.jpg');
Moon = imread('Moon.jpg');
Rice = imread('Rice.jpg');

%-------------------------------------------------------------------------
%Problem 1
%-------------------------------------------------------------------------

wghtdAvIm = AverageFiltering(Circ,wghtd);
stndrdAvIm = AverageFiltering(Circ,stndrd);


figure 
subplot(1,3,1), subimage(Circ), title('Circuit.jpg')
subplot(1,3,2), subimage(wghtdAvIm), title('Weighted Averaging Mask')
subplot(1,3,3), subimage(stndrdAvIm), title('Standard Averaging Mask')

disp('-----Finish Solving Problem 1.1-----')
pause

 wghtdMedIm = MedianFiltering(Circ,wghtd);
 stnMedIm = MedianFiltering(Circ,stndrd);

figure 
subplot(1,3,1), subimage(Circ), title('Circuit.jpg')
subplot(1,3,2), subimage(wghtdMedIm), title('Weighted Meadian Filtering')
subplot(1,3,3), subimage(stnMedIm), title('Standard Meadian Filtering')

disp('-----Finish Solving Problem 1.2-----')
pause


FilteredIm = conv2(Moon,lapl,'same');

scaledFilteredIm = FilteredIm-min(FilteredIm(:));
scaledFilteredIm = scaledFilteredIm*(255.0/max(scaledFilteredIm(:)));

dMoon = double(Moon);

dMoon  = dMoon - min(dMoon(:));
dMoon  = dMoon *(255.0/max(dMoon(:)));

EnhancedMoon = dMoon - FilteredIm;


figure 
subplot(2,2,1), subimage(Moon), title('Moon.jpg')
subplot(2,2,2), subimage(uint8(FilteredIm)), title('Filtered Moon')
subplot(2,2,3), subimage(uint8(scaledFilteredIm)), title('Scaled Filtered Moon')
subplot(2,2,4), subimage(uint8(EnhancedMoon)), title('Enhanced Moon')

disp('-----Finish Solving Problem 1.3-----')
pause

%-------------------------------------------------------------------------
%Problem 2
%-------------------------------------------------------------------------

[r,c]=size(Rice);
imThresh = zeros(r,c);
imThresh(Rice(:,:)>=110)=1;


imGx = imfilter(imThresh, Gx,'conv');
imGy = imfilter(imThresh, Gy,'conv');
imG(:,:) = abs(imGx(:,:))+abs(imGy(:,:));

[r,c]=size(Rice);
imThresh(r,c) = double(0.0);
imThresh(Rice(:,:)>=110)=1.0;


imGx = imfilter(imThresh, Gx,'conv');
imGy = imfilter(imThresh, Gy,'conv');
imG(:,:) = abs(imGx(:,:))+abs(imGy(:,:));


disp('To determine the threshold for Rice.jpg I looked for the minima right of the maxima in the Rice histogram because this threshold represents the threhold between the lighter colored rice on the darker background.')

h = CalEdgeHist(Rice, 20);

figure
subplot(1,3,1), subimage(Rice), title('Rice.jpg')
subplot(1,3,2), subimage(imG), title('Rice Edges')
subplot(1,3,3), bar(1:20,h), title('Rice Edge Angle Histogram')

disp('-----Finish Solving Problem 2-----')
pause

%-------------------------------------------------------------------------
%Problem 3
%-------------------------------------------------------------------------

text = imread('Text.gif');

t=clearStreaks(text);




figure
imshow(t)

disp('-----Finish Solving Problem 3-----')
pause
clear;
close all;