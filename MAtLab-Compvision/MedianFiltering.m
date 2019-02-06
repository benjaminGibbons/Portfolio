%Ben Gibbons Assignment 3
function filteredIm=MedianFiltering(im,mask)

[dim,dim2] = size(mask);
imDim = size(im);
%check mask dimensions
if (dim~=dim2)
    disp('dimensions of mask must be square m=n')
    return 
elseif(mod(dim,2)==0||mod(dim2,2)==0)
    disp('dimensions of mask must be odd n%2!=0')
    return 
end

mask = mask(:);

%pad im with zeros where pad = ceiling mask dim/2
padSz = uint64(dim-1);

%get start end locations in newIm
s = uint64(1+(padSz/2));
xe = uint64(imDim(1)+(padSz/2));
ye = uint64(imDim(2)+(padSz/2));

%make padded im
newIm(imDim(1)+padSz,imDim(2)+padSz)= uint8(0);
newIm(s:xe, s:ye)=im(:,:);

weightVec=255;
%apply mask 
for i = 1:imDim(1)
    for j = 1:imDim(2)
        %get submatrix
        submat = newIm(i:i+dim-1,j:j+dim-1);
        submat=submat(:);
       %find weighted median
        for k = 1:dim^2
            for l = 1:mask(k)
             weightVec=[weightVec, submat(k)];   
            end
        end
        filteredIm(i,j) = median(weightVec);
        weightVec = 255; 
    end
end
end