
subroutine calc_pot(pos,optpos,pot,arraylength,N,Nopt)
  implicit none
  integer, intent(in) :: N
  integer, intent(in) :: arraylength
  real(8), intent(in) :: pos(arraylength, 2)
  integer, intent(in) :: Nopt
  real(8), intent(inout) :: pot(Nopt)
  !f2py intent(in, out) pot
  real(8), intent(in) :: optpos(Nopt, 2)
  real(8) :: delta_r(2), dr2
  real(8), parameter :: rmax = 3.2_8
  real(8), parameter :: sigma = 0.8, foureps = 1.0
  integer :: i, j
  do i = 1, Nopt
  pot(i) = 0.0
    do j=1,N-1
      delta_r = optpos(i,:) - pos(j,:)
      dr2 = dot_product(delta_r,delta_r)
      dr2 = sigma/dr2
      pot(i)=pot(i)+foureps*(dr2**6 - dr2**3) 
    end do
  end do
end subroutine
