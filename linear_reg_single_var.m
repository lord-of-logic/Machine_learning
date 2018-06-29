clc
clear all

% Load data
data = load('ex1data1.txt');
X = data(:, 1); y = data(:, 2);
m = length(y); % number of training examples

% Visualize the data
figure; % open a new figure window
plot(X,y,'rx','MarkerSize',10)
xlabel('Population of City in 10000s');
ylabel('Profit in $10000s');

% Init the variables
X = [ones(m, 1), data(:,1)]; % Add a column of ones to x
theta = zeros(2, 1); % initialize fitting parameters
num_iters = 1500;
alpha = 0.01;

% Initial cost function value
J = sum((X*theta-y).^2)/(2*m);
fprintf('With theta = [0 ; 0]\nCost computed = %f\n', J);

% Batch Gradient descent
J_history = zeros(num_iters, 1);

for iter = 1:num_iters
    cost=computeCost(X,y,theta)
    temp_theta=theta;
    theta(1)=theta(1)-(alpha/m)*sum((X*temp_theta-y).*X(:,1:1));
    theta(2)=theta(2)-(alpha/m)*sum((X*temp_theta-y).*X(:,2:2));
end

fprintf('Theta found by gradient descent:\n');
fprintf('%f\n', theta);

hold on; % keep previous plot visible
plot(X(:,2), X*theta, '-')
legend('Training data', 'Linear regression')
hold off

predict1 = [1, 3.5] *theta;
fprintf('For population = 35,000, we predict a profit of %f\n',...
    predict1*10000);
predict2 = [1, 7] * theta;
fprintf('For population = 70,000, we predict a profit of %f\n',...
    predict2*10000);
