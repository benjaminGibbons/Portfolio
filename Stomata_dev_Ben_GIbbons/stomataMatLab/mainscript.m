ball=imread('Stomata.png');
se1 = strel('square',5);
ball1 = imerode(ball,se1);
imwrite(ball1, 'erod.png');
ball2 = im2bw(ball1,.25);
imwrite(ball2, 'bw.png');
BW = gpuArray(ball2);

s = regionprops(BW, 'centroid');

centroids = cat(1, s.Centroid);
imshow(ball2);
hold on
plot(centroids(:,1), centroids(:,2), 'b*')
hold off

D = pdist(centroids, 'euclidean'); 
M = mean(D);



%se1=strel('square',3);

%[ labelIm, num ] = FindComponentLabels(ball2,se1);

%disp(num);