%Ben Gibbons Assignment 3
function clearIm  = clearStreaks( im)
t= im;

imTx=medfilt2(im,[9 9]);

[r,c]=size(im);
imT(r,c) = uint8(0);
imT(imTx(:,:)>=225)=255;

t(imT(:,:)==255)=0;
t(t(:,:)>75)=255;

at = im+t;
clearIm=at;

end

