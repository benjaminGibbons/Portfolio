%Ben Gibbons Assignment 3

function edgeHist = CalEdgeHist( im, bin )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here


Gx = [-1 0 1; -2 0 2; -1 0 1];
Gy = [1 2 1; 0 0 0; -1 -2 -1];


bins(1,bin) = uint64(0);

[r,c]=size(im);

imTheta(r,c)=double(0);

[r,c]=size(im);
imThresh(r,c) = double(0.0);
imThresh(im(:,:)>=110)=1.0;

imGx = imfilter(imThresh, Gx,'conv');
imGy = imfilter(imThresh, Gy,'conv');

imTheta(:,:)=atan(imGy(:,:)./imGx(:,:));


mx = max(imTheta(:));
mn = min(imTheta(:));
bSz = (mx-mn)/bin;
rLo = mn;
rHi = bSz; 

for i = 1:bin
    
mn=sum(imTheta(:)<rLo);
mx=sum(imTheta(:)<=rHi);

bins(i)=mx-mn;

rLo=rLo+bSz;
rHi=rHi+bSz;
end

edgeHist = bins;


end

